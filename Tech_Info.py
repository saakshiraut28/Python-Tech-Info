# Author : Saakshi_Raut
# Date(MM/DD/YY) : 4/12/2020
# Tech-info


def cloud():
    print('''
      Cloud Computing:
      It is the practice of using a network of remote servers hosted on the Internet store, manage, and
      process data, rather than a local server or a personal computer.    
    ''')


def iot():
    print('''
      Internet Of Things: 
      The Internet of things (IoT) is a system of interrelated computing devices, mechanical and digital
      machines provided with unique identifiers (UIDs) and the ability to transfer data over a network 
      without requiring human-to-human or human-to-computer interaction.
    ''')


def hacking():
    print('''''Ethical Hacking: 
     Ethical hacking and ethical hacker are terms used to describe hacking performed
     by a company or individual to help identify potential threats on a computer or network. An ethical hacker 
     attempts to bypass system security and search for any weak points that could be exploited by malicious 
     hackers.
     ''''')


def edge_computing():
    print('''
    Edge Computing:
    Edge computing is a distributed computing paradigm which brings computation and data storage closer to the 
    location where it is needed, to improve response times and save bandwidth.''')


def quantum_computing():
    print(''''
    Quantum Computing:
    Quantum computing is the use of quantum-mechanical phenomena such as superposition and entanglement to perform 
    computation. Computers that perform quantum computation are known as a quantum computers.
    ''''')


print('''
       INDEX 
   1.Cloud Computing
   2.IOT
   3.Ethical Hacking
   4.Edge Computing
   5.Quantum Computing
   ___________
   6.QUIT
''')
print("(Enter the serial number of topic:)")
while True:
    choice = int(input(">>>"))
    if choice == 1:
        cloud()
    elif choice == 2:
        iot()
    elif choice == 3:
        hacking()
    elif choice == 4:
        edge_computing()
    elif choice == 5:
        quantum_computing()
    elif choice == 6:
        print('Quit')
        break
    else:
        print('Invalid Input. Check the index no. of the title.')