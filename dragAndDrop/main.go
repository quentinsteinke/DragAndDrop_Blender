package main

import "C"

//export DragAndDrop
func DragAndDrop() *C.char {
	return C.CString("Hello from Go!")
}

func main() {}
