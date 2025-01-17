Reading Attendance Data:

The program reads an attendance file that contains information about different people, such as their name, contact number, and entry/exit times.
It stores this information in a structured format, where each person's name is a key, and their contact and time details are stored as values.
Reading Suspicious People List:

The program reads another file that lists people considered suspicious, storing the names of these individuals in a list.
Identifying Overlapping Contacts:

For each person in the suspicious list, the program checks if their entry and exit times overlap with others in the attendance list.
If two people's times overlap (i.e., if one person entered during the other person's presence or if their exit times coincide), it considers them as being in contact.
These contacts are flagged as suspicious.
Output:

The program then prints out the names and contact numbers of people who were in contact with suspicious individuals during overlapping times.
The overall flow of the program is:

Read the attendance data and store it.
Read the list of suspicious people.
Compare each suspicious person’s timings with others to find overlapping times.
Display the people who were in contact during the overlap, along with their contact numbers.
