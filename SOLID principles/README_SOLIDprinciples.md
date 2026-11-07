# SOLID Principles: The Complete Guide to Object-Oriented Design

The **SOLID** principles are five foundational design guidelines formulated by Robert C. Martin ("Uncle Bob") to build maintainable, scalable, understandable, and testable object-oriented software.

---

## Table of Contents
1. [Overview & Quick Reference](#overview--quick-reference)
2. [S — Single Responsibility Principle (SRP)](#1-single-responsibility-principle-srp)
3. [O — Open/Closed Principle (OCP)](#2-openclosed-principle-ocp)
4. [L — Liskov Substitution Principle (LSP)](#3-liskov-substitution-principle-lsp)
5. [I — Interface Segregation Principle (ISP)](#4-interface-segregation-principle-isp)
6. [D — Dependency Inversion Principle (DIP)](#5-dependency-inversion-principle-dip)
   - [Architectural Flow](#architectural-flow)
   - [The 5-File Modular Implementation](#the-5-file-modular-implementation)
   - [Signature Consistency in Abstract Implementations](#signature-consistency-in-abstract-implementations)
7. [Code Smells & Quick Detection Cheat Sheet](#code-smells--quick-detection-cheat-sheet)

---

## Overview & Quick Reference

| Principle | Primary Rule | Core Goal | Primary Warning Sign |
|---|---|---|---|
| **S** - Single Responsibility | A class should have one, and only one, reason to change. | High cohesion | A class that handles persistence, UI, and business rules at once. |
| **O** - Open/Closed | Open for extension, closed for modification. | Safe additions without regressions | Long `if-elif-else` or `switch` statements checking entity types. |
| **L** - Liskov Substitution | Subtypes must be substitutable for their base types. | Predictable polymorphism | Overridden methods raising `NotImplementedError` or returning unexpected types. |
| **I** - Interface Segregation | Clients should not depend on interfaces they do not use. | Lean, focused interfaces | Classes forced to implement dummy methods or empty passes. |
| **D** - Dependency Inversion | Depend on abstractions, not concrete implementations. | Loose coupling | Direct instantiation (`MyService()`) inside business logic. |

---

## 1. Single Responsibility Principle (SRP)

> *"A class should have one, and only one, reason to change."*

Every module, class, or function should be responsible for a single piece of functionality and encapsulate only the data and behavior relevant to that purpose.

### The Problem: The "God Object"
In this anti-pattern, the `Invoice` class handles financial calculations, presentation rendering, and database persistence.

```python
class Invoice:
    def __init__(self, items: list[dict], customer: str):
        self.items = items
        self.customer = customer

    def calculate_total(self) -> float:
        return sum(item["price"] * item["qty"] for item in self.items)

    def print_invoice(self) -> None:
        # UI / Presentation concern
        print(f"--- Invoice for {self.customer} ---")
        for item in self.items:
            print(f"- {item['name']}: ${item['price']:.2f} x {item['qty']}")
        print(f"Total: ${self.calculate_total():.2f}")

    def save_to_database(self) -> None:
        # Persistence concern
        print(f"Connecting to SQL DB and saving invoice for {self.customer}...")
```

**Why this fails:**
- If the output format changes (e.g., HTML or PDF instead of terminal text), `Invoice` must change.
- If the database changes (e.g., from SQL to MongoDB), `Invoice` must change.
- Changes to one concern risk breaking unrelated functionality.

### The Refactored Solution
Split the concerns into distinct, single-purpose classes.

```python
class Invoice:
    """Handles solely domain calculations and invoice data."""
    def __init__(self, items: list[dict], customer: str):
        self.items = items
        self.customer = customer

    def calculate_total(self) -> float:
        return sum(item["price"] * item["qty"] for item in self.items)


class InvoiceFormatter:
    """Handles solely presentation formatting."""
    @staticmethod
    def print_terminal(invoice: Invoice) -> None:
        print(f"--- Invoice for {invoice.customer} ---")
        for item in invoice.items:
            print(f"- {item['name']}: ${item['price']:.2f} x {item['qty']}")
        print(f"Total: ${invoice.calculate_total():.2f}")


class InvoiceRepository:
    """Handles solely persistence mechanisms."""
    @staticmethod
    def save(invoice: Invoice) -> None:
        print(f"Writing invoice for {invoice.customer} to database...")
```

---

## 2. Open/Closed Principle (OCP)

> *"Software entities should be open for extension, but closed for modification."*

You should be able to add new features or behavior without modifying previously written, tested, and reviewed code.

### The Problem: Modifying Existing Code with Conditionals
Every time a new discount category is introduced, the core calculation method is opened and edited.

```python
class DiscountCalculator:
    def calculate_discount(self, customer_type: str, price: float) -> float:
        if customer_type == "regular":
            return price * 0.05
        elif customer_type == "vip":
            return price * 0.20
        # Adding 'student' forces edits to this existing logic:
        elif customer_type == "student":
            return price * 0.15
        return 0.0
```

**Why this fails:**
- Modifying a central dispatcher increases regression risk for all customer tiers.
- Violates encapsulation by placing all tier logic inside a single monolithic block.

### The Refactored Solution: Polymorphic Strategy
Create an abstraction for customer pricing and implement each tier independently.

```python
from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def get_discount(self, price: float) -> float:
        pass


class RegularCustomer(Customer):
    def get_discount(self, price: float) -> float:
        return price * 0.05


class VIPCustomer(Customer):
    def get_discount(self, price: float) -> float:
        return price * 0.20


# New customer tiers can be added without modifying existing code
class StudentCustomer(Customer):
    def get_discount(self, price: float) -> float:
        return price * 0.15


class DiscountCalculator:
    def calculate_discount(self, customer: Customer, price: float) -> float:
        return customer.get_discount(price)
```

---

## 3. Liskov Substitution Principle (LSP)

> *"Subtypes must be substitutable for their base types without altering the correctness of the program."*

If class `B` is a subtype of class `A`, code written to use `A` should accept `B` without needing to perform type checks, without triggering unexpected exceptions, and without experiencing unexpected side effects.

### The Problem: Violating Base Class Contracts
An `Ostrich` is biologically a bird, but inheriting a `.fly()` method breaks the expectations established by the base class.

```python
class Bird:
    def fly(self) -> str:
        return "Flying high in the sky"


class Ostrich(Bird):
    def fly(self) -> str:
        # Breaks caller expectations by throwing an exception
        raise NotImplementedError("Ostriches cannot fly!")


def execute_flight(bird: Bird) -> None:
    # Caller expects every Bird to fly safely
    print(bird.fly())

# execute_flight(Ostrich())  # Crashes the application
```

### The Refactored Solution: True Polymorphic Modeling
Group behavior based on actual capabilities rather than purely everyday linguistic classification.

```python
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self) -> str:
        pass


class FlyingBird(Bird, ABC):
    @abstractmethod
    def fly(self) -> str:
        pass

    def move(self) -> str:
        return self.fly()


class Eagle(FlyingBird):
    def fly(self) -> str:
        return "Soaring across mountain peaks"


class Ostrich(Bird):
    def move(self) -> str:
        return "Sprinting across the savanna"


def make_bird_move(bird: Bird) -> None:
    # Works consistently for all subtypes of Bird
    print(bird.move())
```

---

## 4. Interface Segregation Principle (ISP)

> *"Clients should not be forced to depend upon interfaces they do not use."*

Large, bloated interfaces ("fat interfaces") should be split into smaller, more granular interfaces. Classes should only implement the methods they actually support.

### The Problem: The "Fat" Interface
Forcing a simple printer to implement scanning and faxing features.

```python
from abc import ABC, abstractmethod

class MultiFunctionMachine(ABC):
    @abstractmethod
    def print_content(self, document: str) -> None:
        pass

    @abstractmethod
    def scan_content(self, document: str) -> None:
        pass

    @abstractmethod
    def fax_content(self, document: str) -> None:
        pass


class BasicPrinter(MultiFunctionMachine):
    def print_content(self, document: str) -> None:
        print(f"Printing: {document}")

    def scan_content(self, document: str) -> None:
        # Forced to implement unusable method
        raise NotImplementedError("Basic printers cannot scan.")

    def fax_content(self, document: str) -> None:
        # Forced to implement unusable method
        raise NotImplementedError("Basic printers cannot fax.")
```

### The Refactored Solution: Role Interfaces
Decompose the fat interface into distinct, single-purpose roles that can be composed as needed.

```python
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_content(self, document: str) -> None:
        pass


class Scannable(ABC):
    @abstractmethod
    def scan_content(self, document: str) -> None:
        pass


class Faxable(ABC):
    @abstractmethod
    def fax_content(self, document: str) -> None:
        pass


# 1. Simple implementation: only implements what it can do
class BasicPrinter(Printable):
    def print_content(self, document: str) -> None:
        print(f"Printing: {document}")


# 2. Advanced implementation: composes multiple role interfaces
class EnterpriseCopier(Printable, Scannable, Faxable):
    def print_content(self, document: str) -> None:
        print(f"Laser printing: {document}")

    def scan_content(self, document: str) -> None:
        print(f"High-res scan: {document}")

    def fax_content(self, document: str) -> None:
        print(f"Transmitting fax: {document}")
```

---

## 5. Dependency Inversion Principle (DIP)

> *"1. High-level modules should not depend on low-level modules. Both should depend on abstractions."*  
> *"2. Abstractions should not depend on details. Details should depend on abstractions."*

High-level business rules should never be tightly coupled to concrete transport channels, frameworks, databases, or third-party APIs.

### Architectural Flow

```text
CONVENTIONAL TIGHT COUPLING (Bad):
┌─────────────────────────┐
│   NotificationService   │ (High-level policy)
└────────────┬────────────┘
             │ directly imports & instantiates
             ▼
┌─────────────────────────┐
│      EmailService       │ (Low-level detail)
└─────────────────────────┘


DEPENDENCY INVERSION (Good):
┌─────────────────────────┐
│   NotificationService   │ (High-level policy)
└────────────┬────────────┘
             │ depends on
             ▼
    <<abstract interface>>
   [ NotificationChannel ]
             ▲
             │ implements
    ┌────────┴────────┐
    │                 │
┌───┴──────────┐   ┌──┴──────────┐
│ EmailService │   │  SMSService │ (Low-level details)
└──────────────┘   └─────────────┘
```

---

### The 5-File Modular Implementation

In a professional architecture, DIP decouples responsibilities into separate files: an abstraction, individual concrete services, the business logic orchestrator, and an application composition root.

```text
dip_example/
├── notification_channel.py  # 1. The Interface / Abstraction
├── email_service.py         # 2. Concrete Delivery Channel A
├── sms_service.py           # 3. Concrete Delivery Channel B
├── notification_service.py  # 4. High-Level Business Orchestrator
└── main.py                  # 5. Composition Root / Application Entry
```

#### File 1: `notification_channel.py` (The Abstraction)
Defines the strict operational contract without concerning itself with implementation details.

```python
# notification_channel.py
from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        """Contract: Any notification channel must implement this exact signature."""
        pass
```

#### File 2: `email_service.py` (Concrete Detail A)
Implements delivery via email protocols.

```python
# email_service.py
from notification_channel import NotificationChannel

class EmailService(NotificationChannel):
    def send(self, message: str) -> None:
        print(f"[EMAIL] Delivering message: '{message}' via SMTP server.")
```

#### File 3: `sms_service.py` (Concrete Detail B)
Implements delivery via cellular SMS gateways.

```python
# sms_service.py
from notification_channel import NotificationChannel

class SMSService(NotificationChannel):
    def send(self, message: str) -> None:
        print(f"[SMS] Delivering message: '{message}' via Telephony API.")
```

#### File 4: `notification_service.py` (High-Level Policy)
Coordinates business actions. It **never** imports `email_service.py` or `sms_service.py`; it depends solely on `NotificationChannel`.

```python
# notification_service.py
from notification_channel import NotificationChannel

class NotificationService:
    def __init__(self, channel: NotificationChannel):
        # Dependency is injected from the outside (Constructor Injection)
        self.channel: NotificationChannel = channel

    def notify(self, message: str) -> None:
        # Business policy: logging, validation, rate limiting, then sending
        sanitized_message = message.strip()
        self.channel.send(sanitized_message)
```

#### File 5: `main.py` (Composition Root)
Wires dependencies together at runtime.

```python
# main.py
from email_service import EmailService
from sms_service import SMSService
from notification_service import NotificationService

if __name__ == "__main__":
    # 1. Send via Email Channel
    email_channel = EmailService()
    user_alert_service = NotificationService(channel=email_channel)
    user_alert_service.notify("Welcome to our service!")

    # 2. Swap out channel for SMS without touching NotificationService code
    sms_channel = SMSService()
    security_alert_service = NotificationService(channel=sms_channel)
    security_alert_service.notify("Your verification code is: 849201")
```

---

### Signature Consistency in Abstract Implementations

When overriding abstract methods in derived classes, adhere to consistent method signatures:

```python
# Abstract Method Definition:
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass
```

#### 1. Why Renaming Parameters Breaks Code
Python resolves keyword arguments using exact variable names. If a child renames `message` to `body`:

```python
class EmailService(NotificationChannel):
    def send(self, body: str) -> None:  # Renamed 'message' to 'body'
        print(body)

# Call via Interface using keyword argument:
channel: NotificationChannel = EmailService()
channel.send(message="System Update")
# TypeError: EmailService.send() got an unexpected keyword argument 'message'
```

#### 2. Rules for Derived Class Method Signatures

| Adjustment | Safe in Child? | Impact / Explanation |
|---|---|---|
| **Same parameter name & order** (`send(self, message)`) | **Yes** | Fully compliant with callers, linters, and type checkers. |
| **Renamed parameter** (`send(self, body)`) | **No** | Breaks keyword-argument calling (`send(message=...)`). Violates LSP. |
| **Adding mandatory parameter** (`send(self, message, to)`) | **No** | Breaks existing callers passing only `message`. |
| **Adding optional parameter** (`send(self, message, priority=1)`) | **Yes** | Safe. Callers supplying only `message` continue working uninterrupted. |

---

## Code Smells & Quick Detection Cheat Sheet

```text
SYMPTOM / CODE SMELL                                  VIOLATED PRINCIPLE   CORRECTIVE REFACTORING
---------------------------------------------------------------------------------------------------------------------------
A class handles domain logic, SQL, and UI rendering   Single Responsibility (SRP)   Split into Domain, Repository, and Formatter.
Switch/if statements checking type to decide logic    Open/Closed (OCP)             Extract base interface and use Polymorphism.
Overridden subclass method raises NotImplementedError Liskov Substitution (LSP)     Redesign inheritance tree or split contracts.
Subclass must implement dummy/empty methods           Interface Segregation (ISP)   Break large interfaces into small role traits.
Direct class instantiation inside business logic      Dependency Inversion (DIP)    Inject an abstract interface via constructor.
```