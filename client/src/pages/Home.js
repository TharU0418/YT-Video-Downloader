import React, { useEffect, useState } from 'react';
import axios from 'axios';


function Home() {
    const [link, setLink] = useState('');

    const[data, setData] = useState({title:"",
                                    thumbnail:""})

    useEffect(() => {
        if(link){
            console.log("fetch")
        fetch("http://localhost:5000/data", {
            method:"POST",
            headers:{
                "Content-Type": "application/json",
            },
            body:JSON.stringify({inputLink:link}),
        })
            .then((res) => res.json())
            .then((data) => {
                
                setData({title:data.Vid_title,
                        thumbnail:data.Thumbnail_url});
                console.log("id",data.Vid_title);
            });
        }
    }, [link]);

    const download = async (e) => {

        e.preventDefault();
        console.log(link);

        const response = await axios.post("http://localhost:5000/data", {
            inputLink: link
        });
        
    };

    return (
        <div className='Home'>
            
            <h2>NextWay YouTube Video Downloader</h2>
            <form>
                <input type='url' onChange={(e) => setLink(e.target.value)} placeholder='Paste Link Here' />
                <button onClick={download}>Download</button>
                <h2>"Title" ,{data.title}</h2>
                <img src={data.thumbnail} />
            </form>
        </div>
    );
}

export default Home;