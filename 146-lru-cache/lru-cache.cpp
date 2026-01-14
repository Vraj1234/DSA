struct Node{
    int key, val;
    Node* prev;
    Node* next;
    Node(int k, int v): key(k), val(v), prev(nullptr), next(nullptr){};
};

class LRUCache {
public:
    int cap;
    unordered_map<int, Node*> mp;
    Node* head = new Node(-1,-1);
    Node* tail = new Node(-1,-1);
    LRUCache(int capacity) {
        cap = capacity;
        head->next = tail;
        tail->prev = head;
    }
    



    void addNodeAtTail(Node* node){
        Node* temp;
        temp = tail->prev;
        temp->next = node;
        node->next = tail;
        node->prev = temp;
        tail->prev = node;
    }

    void removeNode(Node* node){
        Node* temp1 = node->prev;
        Node* temp2 = node->next;
        temp1->next = temp2;
        temp2->prev = temp1;
    }

    int get(int key) {
        if(mp.find(key)!= mp.end()){
            removeNode(mp[key]);
            addNodeAtTail(mp[key]);
            return mp[key]->val;
        } else{
            return -1;
        }  
    }
    
    void put(int key, int value) {
        if(mp.find(key)!= mp.end()){
            mp[key]->val = value;
            Node* updatedNode = mp[key];
            removeNode(updatedNode);
            addNodeAtTail(updatedNode);
        }else {
            Node* nodeToAdd = new Node(key, value);
            if(cap!=0){
                addNodeAtTail(nodeToAdd);
                mp.insert({key, nodeToAdd});
                cap--;
            }else{
                mp.erase(head->next->key);
                removeNode(head->next);
                addNodeAtTail(nodeToAdd);
                mp.insert({key, nodeToAdd});
            } 
        }     
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */