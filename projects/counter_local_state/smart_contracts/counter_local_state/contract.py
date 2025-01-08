from algopy import ARC4Contract, Global,Txn, UInt64, LocalState
from algopy.arc4 import abimethod

class CounterLocalState(ARC4Contract):

    def __init__(self)->None:
        self.counter = LocalState(UInt64)

    @abimethod
    def increment(self)->None:
        assert Txn.sender.is_opted_in(Global.current_application_id), "Must opt-in to call"
        self.counter[Txn.sender] += 1

    @abimethod
    def decrement(self)-> None:
        assert Txn.sender.is_opted_in(Global.current_application_id), "Must opt-in to call"
        self.counter[Txn.sender] -= 1

    @abimethod()
    def get(self) -> UInt64:
        assert Txn.sender.is_opted_in(Global.current_application_id), "Must opt in to call"
        return self.counter[Txn.sender]
    
    @abimethod(allow_actions=['OptIn'])
    def opt_in(self) -> None:
        self.counter[Txn.sender] = UInt64(0)