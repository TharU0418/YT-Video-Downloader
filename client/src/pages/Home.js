import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Home() {
    const [link, setLink] = useState('');

    const[data, setData] = useState({title:""})

    useEffect(() => {
        fetch("/data")
            .then((res) => res.json())
            .then((data) => {
                setLink(data.vid_title);
                console.log(data.vid_title);
            });
    }, []);

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
                <h2>"Title" ,{data.vid_title}</h2>
            </form>
        </div>
    );
}

export default Home;