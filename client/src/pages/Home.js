import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Col, Container, Dropdown, DropdownButton, Form, Row } from 'react-bootstrap';


function Home() {
    const [link, setLink] = useState('');

    const[data, setData] = useState({title:"",
                                    thumbnail:""})

    const[videoQuality, setVideoQuality] = useState("360");

    const handleVideoQuality = (quality) => {
        setVideoQuality(quality);
    }

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

    const LoadDetails = async (e) => {

        e.preventDefault();
        console.log(link);

        const response = await axios.post("http://localhost:5000/data", {
            inputLink: link
        });
        
    };

    const handleDownload = async (e) => {
         e.preventDefault();
         console.log("🚀 ~ file: Home.js:57 ~ handleDownload ~ videoQuality:", videoQuality)

         const response = await axios.post("http://localhost:5000/data2", {
             inputLink: link,
             videoQuality:videoQuality
         });
             
    }

    return (
        <div className='Home'>
            
            <h2>NextWay YouTube Video Downloader</h2>
            <div className='para'>
            <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam nibh massa, euismod quis nunc at, 
                imperdiet aliquam tortor. Cras lectus odio, eleifend eget fringilla id, bibendum in risus. Quisque dictum 
                neque at ex venenatis varius. Fusce in risus malesuada, pellentesque leo ornare, pellentesque purus. Nam laoreet 
                mauris sed euismod faucibus. Maecenas justo dolor, vestibulum quis velit eget, aliquet semper est. Vestibulum 
                iaculis gravida nulla non porta. Pellentesque fermentum, dolor et pretium placerat, eros nibh tempor nibh, et 
                ultrices tellus arcu at nisi. Phasellus sed erat tempus, convallis purus sit amet, sollicitudin nisi. Curabitur 
                eu pellentesque metus. Vestibulum eget tincidunt nisi.
            </p>
            </div>
            <form>
                <input type='url' onChange={(e) => setLink(e.target.value)} className='input-box' placeholder='Paste Link Here' />
                <button onClick={LoadDetails}>Load</button>
            </form>

            <div className='yt-results'>
                <div className='left'>
                    <h2>"Title" ,{data.title}</h2>
                    <img src={data.thumbnail} width={'360px'} height={'200px'}/>
                </div>
                <div className='right'>
                    <Container>
                        <Row>
                        <Col>
                            <Form.Group
                                style={{
                                    color:'white',
                                }}
                            >
                                <Form.Label>
                                Video Quality
                                </Form.Label>
                            </Form.Group>
                            </Col>
                            <Col> 
                        <DropdownButton
                        id="quality-of-video"
                        title={`${videoQuality}`}
                        variant="secondary"
                        style={{
                            color:'white',
                            marginBottom:"20px",
                            minWidth:'50px'
                        }}
                    >
                        <Dropdown.Item
                            onClick={() =>
                                handleVideoQuality("144p")
                            }
                        >
                            144p
                        </Dropdown.Item>
                        <Dropdown.Item
                            onClick={() =>
                                handleVideoQuality("240p")
                            }
                        >
                            240p
                        </Dropdown.Item>
                        <Dropdown.Item
                            onClick={() =>
                                handleVideoQuality("360p")
                            }
                        >
                            360p
                        </Dropdown.Item>
                        <Dropdown.Item
                            onClick={() =>
                                handleVideoQuality("720p")
                            }
                        >
                            720p
                        </Dropdown.Item>
                        <Dropdown.Item
                            onClick={() =>
                                handleVideoQuality("1080p")
                            }
                        >
                            1080p
                        </Dropdown.Item>
                        <Dropdown.Item
                            onClick={() =>
                                handleVideoQuality("MP3")
                            }
                        >
                            MP3
                        </Dropdown.Item>
                    </DropdownButton>
                    </Col>
                        </Row>
                        <Row>
                            <button type='submit' onClick={handleDownload}>DOWNLOAD</button>
                        </Row>
                    </Container>
                </div>
                
            </div>
            

        </div>
    );
}

export default Home;