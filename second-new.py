class Node:                                                                     
     def __init__(self, val, prev_ref, next_ref):                               
         self.val = val;                                                        
         self.prev = prev_ref;                                                  
         self.next = next_ref;                                                    
                                                                                
       
                                                                         
head = tail = None;                                                             
         
                                                                   
def append_node(val):                                                           
    global head, tail;                                                          
    node = Node(val, None, None);                                               
    if head is None:                                                            
        head = node;                                                            
    else:                                                                       
        tail.next = node;                                                       
        node.prev = tail;                                                       
    tail = node;      


def insert_node(val, position):                                                 
    global head, tail;                                                          
    current_node = head;                                                        
    while(position > 1):                                                        
        position -= 1;                                                          
        current_node = current_node.next;                                       
    temp_next = current_node.next;                                              
    node = Node(val, current_node, temp_next);                                  
    current_node.next = node;                                                   
    if(temp_next.next is not None):                                             
        temp_next.prev = node;                                                               
            
                                                                   
def print_list():                                                               
    global head, tail;                                                          
    print("Double linked list");                                                
    current_node = head;                                                        
    print ("head <==>",);                                                         
    while(current_node is not None):                                            
        print (current_node.val, "<==>",);                                        
        current_node = current_node.next;                                       
    print("End");                 
                                              
                                                                              
def remove_node(val):                                                           
    global head, tail;                                                          
    current_node = head;                                                        
    previous_node = None;                                                       
    while(current_node is not None):                                            
        if current_node.val == val:                                             
            if previous_node is not None:                                       
                current_node.next.prev = current_node.prev;                     
                previous_node.next = current_node.next;                         
            else:                                                               
                current_node.next.prev = None;                                  
                head = current_node.next;                                       
        previous_node = current_node;                                           
        current_node = current_node.next;                                     
                            
                                                    
def reverse_linked_list():                                                      
    global head, tail;                                                          
    print("Double linked list reverse order");                                  
    current_node = tail;                                                        
    print( "tail <==>",);                                                         
    while(current_node is not None):                                            
        print (current_node.val, "<==>",);                                        
        current_node = current_node.prev;                                       
    print ("End");   


def count():                                                                    
    global head, tail;                                                          
    current_node = head;                                                        
    counter = 0;                                                                
    while(current_node is not None):                                            
        counter += 1;                                                           
        current_node = current_node.next;                                       
    print ("Double linked list node count:", counter);                            
                                                                                
if __name__ == "__main__":                                                      
    append_node(20);                                                            
    append_node(13);                                                            
    append_node(24);                                                            
    append_node(56);                                                            
    print_list();                                                               
    insert_node(45, 2);                                                         
    print ("After insert node at 2");                                             
    print_list();                                                               
    reverse_linked_list();                                                      
    remove_node(13);                                                            
    print ("After removal of node 13");                                           
    print_list();                                                               
    reverse_linked_list();                                                      
    count();   
