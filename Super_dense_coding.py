
# coding: utf-8

from qiskit import IBMQ, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.qasm import pi
from qiskit.tools.visualization import plot_histogram, circuit_drawer
import numpy as np

APItoken = "Replace me"
url = "Replace me"
IBMQ.enable_account(APItoken, url)

IBMQ.backends()

#Qubits for Alice(the sender)	
ba = 3
#A qubit for Bob(the receiver)
bb = 1
cn = 2

qa = QuantumRegister(ba)
qb = QuantumRegister(bb)
c = ClassicalRegister(cn)
qca = QuantumCircuit(qa,c)
qcb = QuantumCircuit(qb,c)
qc = qca+qcb


#Alice is going to send the 2-qubits state |10>
#So, we need to apply X gate on the first qubit
qc.x(qa[0])
qc.barrier()

qc.h(qa[2])
qc.cx(qa[2],qb[0])
qc.cz(qa[0],qa[2])
qc.cx(qa[2],qb[0])
qc.h(qa[2])

#The first qubit would be 1
qc.measure(qb[0],c[0])

#And the second qubit would be 0
qc.measure(qa[2],c[1])

#Put a real device first and a simulator after that
backends = ['ibmq_20_tokyo', 'qasm_simulator']

#Use this for the actual machine
backend_sim = IBMQ.get_backend(backends[0])
#{'00': 587, '11': 230, '10': 3195, '01': 84}

#Use this for the simulation
#backend_sim = Aer.get_backend(backends[1])
result = execute(qc, backend_sim, shots=4096).result()
#{'10': 4096}

#You can get the quantum circuit in Latex style
#circuit_drawer(qc).show()

print(result.get_counts(qc))
plot_histogram(result.get_counts(qc))
