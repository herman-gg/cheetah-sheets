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
```