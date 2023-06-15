import React from 'react'
import {Nav, Navbar, Container, Form, Button, NavDropdown} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

function NavBar() {
  return (
    <div className='NavBar'>
        <Navbar bg="light" expand="lg" style={{backgroundColor:'white'}}>
            <Container fluid>
            <Navbar.Brand href="/" style={{color:'red'}}>Next-Way</Navbar.Brand>
            <Navbar.Toggle aria-controls="navbarScroll" />
            <Navbar.Collapse id="navbarScroll">
          <Nav
            className="me-auto my-2 my-lg-0"
            style={{ maxHeight: '100px' }}
            navbarScroll
          >
            
          </Nav>

            <Nav>
            <Nav.Link href="#action1">Home</Nav.Link>
            <Nav.Link href="#action2">Link</Nav.Link>
            </Nav>

            </Navbar.Collapse>
      </Container>
    </Navbar>
    </div>
  )
}

export default NavBar