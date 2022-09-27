package modules

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"time"
)

func CreateTask() {
	Clear()

	stdins := bufio.NewReader(os.Stdin)

	fmt.Print("Your task?\nEnter here: ")
	task, err := stdins.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("\nThank you!")

	Time := time.Now()
	shortTime := Time.Format("Mon 06-01-2")

	file, err1 := os.OpenFile("todo.txt", os.O_APPEND|os.O_WRONLY, 0644)
	if err1 != nil {
		log.Fatal(err)
	}

	defer file.Close()

	toWrite := "\n\n" + task + "At: " + shortTime
	_, err2 := fmt.Fprint(file, toWrite)
	if err2 != nil {
		log.Fatal(err2)
	}
}
