## Types

```swift
// Variables vs constants
var a: String = "variable"
let b = "constant" // String type is inferred by type inferrence

// Basic types
var pi: Double = 3.1415
var isTrue: Bool = false

// String interpolation
var s1 = "value of PI is: \(pi)"


// Collection types
// Arrays
let langs = ["swift", "python", "js"]
print(langs[langs.count - 1])

// Sets
// 1. Only unique values
// 2. Order doesn't matter
let langSet = Set(["swift", "python", "js"])


let colors2 = Set(["red", "green", "blue", "red", "blue"]) //-> {"red", "green", "blue"}

// Tuples
let user = (email: "user@app.com", name: "username1")
print(user.0, user.email)
print(user.1, user.name)

// Dicts
let prices = [
  "iPhone 15": 799,
  "iPhone 15 Pro": 1099,
  "iPhone 15 Pro Ultra": 1399
]
prices["iPhone 15"]

// default value
prices["iPhone 14", default: 599]

// Empty collections
let emptyDict = [String: Int]()
let emptySet = Set<Int>()
let emptyArray = Array<Int>()


// Enums
enum Result {
    case success
    case failure
}

let results1 = [Result.success, Result.failure]

var results2 = Array<Result>()
results2.append(.success)

enum Activity {
    case bored
    case running(destination: String)
    case talking(topic: String)
    case singing(song: String)
}
let talking = Activity.talking(topic: "F1")
print(talking)

// Raw values
enum Planet: Int {
    case mercury = 1
    case venus
    case earth
    case mars
}

// --- Conditionals ---

var hungry = true
var vegetarian = false
var isPie = true

if (hungry && !vegetarian) || isPie {
	print("Let's eat!")
}

// Ternary
hungry ? eat() : wait()

// --- Strings concatenation and char checks ---

let lebowski = Cat(name: "Lebowski")
let grPerDay = 150
let daysPerMonth: Double = 30.0

print("\(lebowski.name) eats \(grPerDay * daysPerMonth) food a month")

// Iterate characters in a String
var password = "sneaky-peacky-foxy"
for char in password {
    if char == "-" {
        print("Found '-'")
    }
}

```

## Immutability

An object can be immutable by:
* **by assignment** - when we cannot assign different value to a constant;
* **by value** - value of an object cannot be changed during it's lifetime;

* Two types of types in Swift: `Named` and `Compound` . Types that are considered standard in other languages (like int, bool, string) are actually `named` types in Swift created with structs and can be extended using [Extensions](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/extensions). 
* A _compound type_ is a type without a name, defined in the Swift language itself. There are two compound types: **function** types and **tuple** types.
* ```
```swift
// Type annotations
let someTuple: (Double, Double) = (3.14159, 2.71828)
func someFunction(a: Int) { /* ... */ }
```

* Two types of declarations: `var` and `let` (constants). Contrary to typescript where you cannot declare a const without initializing it at the same place, in Swift you can do it.

```swift
var environment = "development"
let maximumNumberOfLoginAttempts: Int
// maximumNumberOfLoginAttempts has no value yet.

if environment == "development" {
    maximumNumberOfLoginAttempts = 100
} else {
    maximumNumberOfLoginAttempts = 10
}
```

* Declaration of several variables of the same type:
```swift
// Explicitly defined type ...
let a, b, c: Int
// ... or type inferred type
let d = "some string"
```

* Semicolons are optional:
```swift
let cat = "🐱"; print(cat)
```

* Integers
```swift
// --- Integers
var i1: UInt8 // UInt16 UInt32 UInt64
var i2: Int8 // Int16 Int32 Int64

var iMax = UInt8.max
var iMin = UInt8.min

// `Int` type will be of different size depending on the platform 
// (Int32 for 32-bit, Int64 for 64-bit platforms).
// Same if for UInt.
var i11 = Int 
```
* Signed integers can be either positive of negative _(with 1 byte its a range of: -128 - +127)_
* Unsigned integers can only be positive: _(with 1 byte its a range of: 0 - 255)_

* Floating-point nums
```swift
// Float (32-bit)
let f1: Float = 1.3e38

// Double (64-bit)
let d1: Double = 1.3e40
```

### Type Checks & Type Inference
* Swift does type checks during compilation stage;
* **literal** value - value that appears directly in the source code;

* Type Conversion
```swift
// Int <--> Float conversion
let three = 3
let pointOneFourOneFiveNine = 0.14159
let pi = Double(three) + pointOneFourOneFiveNine
let fToI1 = Int(pi)
```

* Type Aliases
```swift
typealias AudioSample = UInt16

var maxAmplitudeFound = AudioSample.min
```

### Tuples
* Also useful as return values for functions which return multiple values at a time
```swift
typealias StatusCode = (Int, String)
let http404Error: StatusCode = (404, "Not Found")

print(type(of: http404Error))
  
// Tuple decomposition
let (statusCode, statusMessage) = http404Error
print("Response status code: [\(statusCode)](\(statusMessage))")

// selective decomposition
let (justStatusCode, _) = http404Error

// access by index
print("Response status code: [\(http404Error.0)](\(http404Error.1))")

// named tuples
let http200Status = (statusCode: 200, description: "OK")
print("Response status code: [\(http200Status.statusCode)](\(http200Status.description))")
```

## Optionals
* Used when the value can be pressent, but can be as well be absent;
```swift
// --- Optionals ---
let possibleNumber = "123"
let convertedNumber: Int? = Int(possibleNumber)
let convertedNumber2: Optional<Int> = Int(possibleNumber)

let absentValue = nil

// Defined optional variable without a value automatically
// set to nil
var someValue: String? // = nil
```
* nil cannot be used with non-optional variables;
* We can use **optional binding** to check optional value
```swift
if let actualNumber = Int(possibleNumber) {
    print("The string \"\(possibleNumber)\" has an integer value of \(actualNumber)")
} else {
    print("The string \"\(possibleNumber)\" couldn't be converted to an integer")
}
```
* We can use the same variable name if the don't need to refer to original value
```swift
if let actualNumber = actualNumber {
    print("The string has an integer value of \(actualNumber)")
}

// OR shorter vertion

if let myNumber {
    print("My number is \(myNumber)")
}

// Fallback value
let msg: String? = "test-message"
print("Received message says ['" + (msg ?? "undefined") + "'].")

// Forced unwrapping
let possibleNumber = "123"
let convertedNumber = Int(possibleNumber)

let number = convertedNumber!
// 👆 this is the short version of this 👇
guard let number = convertedNumber else {
    fatalError("The number was invalid")
}
```
* **Implicitly Unwrapped Optionals** (You can think of an implicitly unwrapped optional as giving permission for the optional to be force-unwrapped if needed.)
```swift
let possibleString: String? = "An optional string."
let forcedString: String = possibleString! // Requires explicit unwrapping


let assumedString: String! = "An implicitly unwrapped optional string."
let implicitString: String = assumedString // Unwrapped automatically

```

## Error Handling
```swift
// Indicate that function MAY throw an error
func makeTransaction() throws { }

// Catch the error in the client code
do {
  try makeTransaction()
  notifyClients()
} catch TransactionError.outOfFunds {
  notifyClientsOutOfFunds()
} catch {
  makeDefaultNotification()
}
```

