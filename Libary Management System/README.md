# Library Management System
Library management system. 

### Aim
- Make it a realtime system with database and request queues to handle conflicting requests,etc.
- Demonstrate data structures and algorithms knowledge.
- Have fun making it :D.

### Ideas

###### Books
- Each books has a name, a list of authors, a list of genres, a price tag and a summary.
- Search by name, authors, genre or price. There may be sales on certain books. Some books may/ may not be available to borrow for a particular membership tier - Free, Premium, All-Access, etc.

###### Users
- Each user has a username and password. Must have a password reset mechanism that mimics 2-FA.
- Each user has their relevant details stored. Number of books currently borrowed is to be stored in this class object. 
- Can borrow books as long as the number of books he/she has borrowed  is less than or equal to that allowed by the user's membership tier, which will be different.
- Can recharge their membership with extra credits if they want to borrow more.

###### Admin
- Admin alone can sign up new users. Must generate a new username and password for them which they are advised to change later.
- List all users and display their details.
