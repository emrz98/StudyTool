import axios from "axios"
class API{
    static createDeck(data, handler){
        axios.post('decks/', data)
        .then(response => handler(response.data))
        .catch(e => alert(e));
    }
}

export default API;