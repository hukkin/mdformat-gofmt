import mdformat


def test_mdformat_integration():
    unformatted_md = """~~~go
package main
import "fmt"
func main() {
fmt.Println("hello world")
}
~~~
"""
    formatted_md = """```go
package main

import "fmt"

func main() {
\tfmt.Println("hello world")
}
```
"""
    assert mdformat.text(unformatted_md, codeformatters={"go"}) == formatted_md
