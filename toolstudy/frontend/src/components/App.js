import React from 'react';
import {useState, useEffect} from 'react';

import axios from 'axios';
function App(){
    const [data, setData] = useState();
    useEffect(() => {
        const getData = () => {
            axios.get('card/')
            .then(response => {
                console.log(response.data);
                setData(response.data)
            }).catch(e => console.log(e));
        }
        getData();

    },[]);
    
    return(

        <pre>{data !== undefined ? data[0].question: "nulo"}</pre>
    );

}

export default App;
