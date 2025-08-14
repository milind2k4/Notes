
### Infix to Postfix

```c
create stack

for each char ch in input {
	if (ch is an operand){
		output ch
	} else if (ch is ')'){
		pop and output tokens until '(' is popped but dont print '('
	} else {
		pop and output tokens until one of lower priority is encountered or a '(' is encountered or stack is empty
		push ch
	}
}

pop and output all the tokens until stack is empty
```


## Tree
Number of binary trees possible (for unlabeled node):

$$N = \frac{ {}^{2n}C_{n} }{ n+1 } = \frac{ \displaystyle {2n \choose n} }{ n+1 }$$
where n is the number of unlabeled nodes.

Structure for Tree Node 

```c
struct node {
	int data;
	struct node *left, *right;
};
```


### Traversal
Pre-order traversal:
```c
void inorder(struct node *root){
	if (root){
		printf("%c ", root->data);
		inorder(root->left);
		inorder(root->right);
	}
}
```

In-order traversal:
```c
void inorder(struct node *root){
	if (root){
		inorder(root->left);
		printf("%c ", root->data);
		inorder(root->right);
	}
}
```

Post-order traversal:
```c
void inorder(struct node *root){
	if (root){
		printf("%c ", root->data);
		inorder(root->left);
		inorder(root->right);
	}
}
```
