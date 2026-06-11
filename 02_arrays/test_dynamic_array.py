"""
Tests para Dynamic Array
"""
from dynamic_array import DynamicArray
import pytest

def test_array_vacio_al_crear():
    # Arrange
    arr = DynamicArray()
    
    # Act (en este caso no hay acción — probamos el estado inicial)
    
    # Assert
    assert arr.size() == 0
    assert arr.capacity() == 1
    assert arr.is_empty()

def test_push_un_elemento():
    #arrange
    arr = DynamicArray()
    #act
    arr.push("A")
    #assert
    assert arr .size() == 1
    assert arr.is_empty() == False
    assert arr.at(0) == "A"
    
def test_at_fuera_de_rango_lanza_indexerror():
    # Arrange
    arr = DynamicArray()
    arr.push("A")  # solo un elemento en posición 0
    
    # Act + Assert
    with pytest.raises(IndexError):
        arr.at(99)  # 99 está fuera de rango, debe lanzar IndexError

def test_at_indice_negativo_lanza_indexerror():
    #Arrange
    arr = DynamicArray()

    #Act + Assert
    with pytest.raises(IndexError):
        arr.at(-1)

def test_pop_devuelve_el_ultimo_elemento():
    #Arrange
    arr = DynamicArray()
    arr.push("A")
    arr.push("B")
    arr.push("C")
    
    #Act
    ultimo = arr.pop()

    #Assert
    assert ultimo == "C"
    assert arr.size() == 2
    assert arr.at(1) == "B"

def test_push_dispara_resize_automatico():
    #Arrange
    arr = DynamicArray()
    
    #Act
    arr.push("A")
    arr.push("B")
    arr.push("C")
    arr.push("D")
    arr.push("E")

    #Assert
    assert arr.size() == 5
    assert arr.capacity() == 8
    assert arr.at(0) == "A"
