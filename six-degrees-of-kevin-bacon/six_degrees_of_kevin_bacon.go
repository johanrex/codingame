package main

import (
	"bufio"
	"container/list"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Pair struct {
	first  string
	second int
}

type Node struct {
	value     string
	neighbors map[string]bool
}

func logDebug(format string, args ...interface{}) {
	fmt.Fprintln(os.Stderr, fmt.Sprintf(format, args...))
}

func parseMovieLine(line string) (string, map[string]bool) {
	tmp := strings.Split(line, ":")
	title := tmp[0]
	actors := strings.Split(tmp[1], ",")
	actorSet := make(map[string]bool)
	for _, actor := range actors {
		actorSet[strings.TrimSpace(actor)] = true
	}
	return title, actorSet
}

func parseInput() (string, map[string]map[string]bool) {
	movies := make(map[string]map[string]bool)

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	sourceActor := scanner.Text()
	scanner.Scan()

	n, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < n; i++ {
		scanner.Scan()
		movieCast := scanner.Text()
		title, actors := parseMovieLine(movieCast)
		movies[title] = actors
	}

	return sourceActor, movies
}

func buildGraph(movies map[string]map[string]bool) map[string]*Node {
	g := make(map[string]*Node)
	for _, actors := range movies {
		for actor := range actors {
			neighbors := make(map[string]bool)
			for neighbor := range actors {
				if neighbor != actor {
					neighbors[neighbor] = true
				}
			}

			if node, ok := g[actor]; ok {
				for neighbor := range neighbors {
					node.neighbors[neighbor] = true
				}
			} else {
				g[actor] = &Node{value: actor, neighbors: neighbors}
			}
		}
	}
	return g
}

func bfs(g map[string]*Node, sourceActor string) int {
	shortestPath := math.MaxInt64

	visited := make(map[string]bool)
	visited[sourceActor] = true

	q := list.New()
	q.PushBack(Pair{sourceActor, 1})

	for q.Len() > 0 {
		e := q.Front()
		q.Remove(e)
		pair := e.Value.(Pair)
		actor := pair.first
		distance := pair.second

		// prune long paths
		if distance > shortestPath {
			continue
		}

		if actor == "Kevin Bacon" {
			shortestPath = distance
		}

		for neighbor := range g[actor].neighbors {
			if !visited[neighbor] {
				visited[neighbor] = true
				q.PushBack(Pair{neighbor, distance + 1})
			}
		}
	}

	return shortestPath
}

func getBaconNr(sourceActor string, g map[string]*Node) int {
	shortestPath := bfs(g, sourceActor)
	baconNr := shortestPath - 1
	return baconNr
}

func main() {
	sourceActor, movies := parseInput()

	//Print parsed input
	logDebug(sourceActor)
	for movie, actors := range movies {
		logDebug("'%s': %v,", movie, actors)
	}

	g := buildGraph(movies)
	baconNr := getBaconNr(sourceActor, g)
	fmt.Println(baconNr)

}
