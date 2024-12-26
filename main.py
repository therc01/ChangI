from utils import store_docs
from utils import get_response

def main():
    
    store_docs('https://www.changiairport.com/')
    print('first website scraped')
    store_docs('https://jewelchangiairport.com/')

    print("Changi Airport Chatbot")
    print("Type 'quit' to exit")
    print("-" * 50)
    
    while True:
        query = input("\nYou: ").strip()
        
        if query.lower() == 'quit':
            break
        
        # Search for relevant documents
        print(get_response(query, 'Changi Airport',"Airport", 'XX'))

if __name__ == "__main__":
    main()