package modules

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func SeeTasks() {
	Clear()

	tasks, err := os.Open("todo.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer tasks.Close()

	contentByte, err2 := ioutil.ReadAll(tasks)
	if err2 != nil {
		log.Fatal()
	}

	contents := string(contentByte)

	fmt.Println(contents)
	fmt.Println("\nThank you!")
}
