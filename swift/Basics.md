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
let langSet = Set(langs)
print(langSet)

let colors2 = Set(["red", "green", "blue", "red", "blue"]) //-> {"red", "green", "blue"}

// Tuples
let user = (email: "user@app.com", name: "username1")
print(user.0, user.email)
print(user.1, user.name)


```