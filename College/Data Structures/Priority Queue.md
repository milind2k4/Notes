Links: 
___
# Priority Queue
#### Struct
```c
struct node {
	int data;
	int priority;
	struct node *next;
};
```

### Create node
```c
struct noede* createNode(int x, int priority){
	struct node *nn = malloc(sizeof(struct node));
	nn->data = x;
	nn->priority = priority;
	nn->next = NULL;

	return nn;
}
```

### Enqueue
```c
enqueue(10, 1);
enqueue(-5, 0);
enqueue(20, 3);
enqueue(30, 2);


(10,1,)-\
(-5,0)->(10,1)-\
(-5,0)->(10,1)->(20,3)-\
(-5,0)->(10,1)->(30,2)->(20,3)-\
```

```c
void enqueue(e, p){
	struct node* nn = createNode(e, p);

	if (front == NULL || p < front->priority){
		nn->next = front;
		front = nn; //insert at beginning
	} else {
		struct node* temp = front;
		while (temp->next != NULL && temp->next->priority <= p){
			temp = temp->next;
		}
		nn->next = temp->next;
		temp->next = nn; //insert in middle
	}
}
```

### Dequeue

```c
void dequeue(){
	if (front == NULL){
		"Underflow";
		return;
	}

	struct node* temp = front;
	front = front->next;
	free(temp);
}
```
