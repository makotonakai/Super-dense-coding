# Super dense coding

Super dense coding is one of the basic protocols of quantum communication. The sender can deliver the information about 2 classical bits by sending the information of just one qubit.  

Let's say Alice has 2 qubits(the bits to send) and Bob has one qubit and there is a shared qubit.  Alice can send the information about 2 qubits by create entanglements by between her 2nd qubit and the shared qubit, and between the shared qubit and Bob's qubit.  

## Mathematical explanation  

Suppose Alice send <img src="https://latex.codecogs.com/gif.latex?|01\rangle" title="|01\rangle" /> state and here is how to send it.  By the way, The first 2 qubits are Alice's,  the 3rd one is the shared one, and the last one is the Bob's.  

<img src="https://latex.codecogs.com/gif.latex?|01\rangle|0\rangle|0\rangle&space;\xrightarrow{I&space;\otimes&space;I&space;\otimes&space;H&space;\otimes&space;I}&space;|01\rangle&space;\frac{|0\rangle&plus;|1\rangle}{\sqrt{2}}|0\rangle&space;\xrightarrow{CNOT_{23}}&space;|01\rangle&space;\frac{|00\rangle&space;&plus;&space;|11\rangle}{\sqrt{2}}&space;\xrightarrow{CZ_{12}}&space;|01\rangle\frac{|00\rangle&space;-&space;|11\rangle}{\sqrt{2}}" title="|01\rangle|0\rangle|0\rangle \xrightarrow{I \otimes H \otimes I} |01\rangle \frac{|0\rangle+|1\rangle}{\sqrt{2}}|0\rangle \xrightarrow{CNOT_{23}} |01\rangle \frac{|00\rangle + |11\rangle}{\sqrt{2}} \xrightarrow{CZ_{12}} |01\rangle\frac{|00\rangle - |11\rangle}{\sqrt{2}}" />  

<img src="https://latex.codecogs.com/gif.latex?\xrightarrow{CNOT_{32}}&space;|01\rangle&space;\frac{|00\rangle&space;-&space;|01\rangle}{\sqrt{2}}&space;=&space;|01\rangle|0\rangle&space;\frac{|0\rangle&space;-&space;|1\rangle}{\sqrt{2}}&space;\xrightarrow{I&space;\otimes&space;I\otimes&space;I&space;\otimes&space;H}&space;|01\rangle|01\rangle" title="\xrightarrow{CNOT_{32}} |01\rangle \frac{|00\rangle - |01\rangle}{\sqrt{2}} = |01\rangle|0\rangle \frac{|0\rangle - |1\rangle}{\sqrt{2}} \xrightarrow{I \otimes I\otimes I \otimes H} |01\rangle|01\rangle" />  

Therefore, Alice successfully delivered <img src="https://latex.codecogs.com/gif.latex?|01\rangle" title="|01\rangle" />.  

## Implementation on Qiskit  
You can implement this calculation in a python called qiskit(https://qiskit.org, python-based quantum computing framework ,which is accessible to IBMQ)  Here is the code you can copy and paste.  
```
ba = 3 #The number of qubits for Alice
bb = 1 #The number of qubits for Bob
cn = 2

qa = QuantumRegister(ba)
qb = QuantumRegister(bb)
c = ClassicalRegister(cn)
qca = QuantumCircuit(qa,c)
qcb = QuantumCircuit(qb,c)
qc = qca+qcb

qc.x(qa[1])
qc.barrier() #Don't forget to put this, otherwise this state would be affected by noise.

qc.h(qa[2])
qc.cx(qa[2],qb[0])
qc.cz(qa[1],qa[2])
qc.cx(qb[0],qa[2])
qc.h(qa[2])

qc.measure(qb[0],c[0])
qc.measure(qa[2],c[1])
```
## Result
Here is the result on the QASM simulator.  
![super_dense_coding_sim](https://user-images.githubusercontent.com/45162150/50749861-12fc8480-1285-11e9-966b-2cb68e6d61e8.png)  
  
Here is also the result on a real device(ibmq_20_tokyo).  
![super_dense_coding_tokyo](https://user-images.githubusercontent.com/45162150/50749890-49d29a80-1285-11e9-9297-b3dbb96f538a.png)



  
  

