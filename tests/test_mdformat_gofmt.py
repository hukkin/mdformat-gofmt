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


def test_gofmt_error(capfd):
    """Test that any prints by gofmt go to devnull."""
    unformatted_md = """~~~go
func {
~~~
"""
    formatted_md = """```go
func {
```
"""
    result = mdformat.text(unformatted_md, codeformatters={"go"})
    captured = capfd.readouterr()
    assert not captured.err
    assert not captured.out
    assert result == formatted_md
