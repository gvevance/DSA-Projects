# Library Management System
Library management system. 

## Aim
- Make it a realtime system with database and request queues to handle conflicting requests,etc.
- Demonstrate data structures and algorithms knowledge.
- Have fun making it :D.

## Ideas

### Books
- Each book has an ID, a name, a list of authors, a list of genres, a price tag and a summary.
- Search by name, authors, genre or price. There may be sales on certain books. Some books may/ may not be available to borrow for a particular membership tier - Free, Premium, All-Access, etc.
- Match every kind of sort or search to the book ID which is the key in a dictionary for fast lookups.

### Users
- Users can sign themselves up by specifying a username and password. If the username entered is not already being used by another member, it can be assigned to him/her. If the password is 'too similar' to the username, do not accept it. Ask them to reconsider. Additionally strenght of the password can also be checked and given back to the user as feedback. 
- Each user has a userID, username and password. The userID is guaranteed to be unique to each member so that must be the key to be used in dictionaries. Must have a password reset mechanism that mimics 2-FA.
- Each user has their relevant details stored. Number of books currently borrowed is to be stored in this class object. 
- Can borrow books as long as the number of books he/she has borrowed is less than or equal to that allowed by the user's membership tier, which will be different.
- Can recharge their membership with extra credits if they want to borrow more.

### Admin
- Admin can sign up new users. New users can also sign themselves up in the console.
- Must generate a new username and password for them which they are advised to change later.
- List all users and display their details.
