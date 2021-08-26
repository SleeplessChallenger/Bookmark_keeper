<h2>Bookmark project</h2>

- In this project I've done a bookmark app that works with CLI<br>
and presents a couple of options to the user

<ul>
	<li>create bookamrk</li>
	<li>list bookmarks by date or date added</li>
	<li>delete bookmark</li>
	<li>update bookmark</li>
	<li>add bookmarks from GitHub</li>
</ul>

<hr>

- About the flow of the program:

1. Architecture:
	<ol>
		<li>presentation layer that gives user the choice to opt</li>
		<li>business layer that handles all the logic between user's choices
		and underlying data</li>
		<li>persistence layer, in my case it's sole database, which keeps all
		all the data</li>

2. I used command pattern to encapsulate logic of commands that will<br>
in turn trigger the actions. Business layer has the abstraction over commands: same `execute` commands. Also you can see that abstract classes were used to ensure every class has realized the method to prevent errors.

3. Database also has interface in `persistence.py`. I did abstract class that makes other classes to realize it. In our case we have db in `models.py`, but to ensure loose coupling I did interface over it as it helps to remove direct connection between <ins>business & persistence</ins> layers, which in turn makes all construction much more malleable.

4. In this project I didn't use ORM, but direct `SQL` statements.

5. In `architecture_principles` you can find files that show correct way
	of implementing various concepts: Inheritance, Composition etc.
	+ you can find `book_notes.txt` where you can read closely
