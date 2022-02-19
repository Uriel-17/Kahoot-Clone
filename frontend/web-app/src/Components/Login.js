import React from 'react'
import { useState } from 'react'
import { 
  Container, 
  Heading,
  FormControl,
  FormLabel,
  FormErrorMessage,
  FormHelperText,
  Input,
  Center,
  Box,
  Stack
} from '@chakra-ui/react'

const Login = () => {

  const [email, setEmail] = useState(''); 
  const [password, setPassword] = useState(''); 


  console.log('email: ', email); 
  console.log('password: ', password); 

  return(

    <Center height='100vh'>
      <Box 
      height= '350px' 
      width = '335px' 
      boxShadow='0px 3px 3px -2px rgb(0 0 0 / 20%), 0px 3px 4px 0px rgb(0 0 0 / 14%), 0px 1px 8px 0px rgb(0 0 0 / 12%)'
      borderRadius='0.6rem'
      >
      <Container maxW='md' centerContent mt='25px' p = '10px'>
        <Heading size = 'md' as = 'h5'>Login</Heading>
        <Center>
          <FormControl isRequired mt='25px'>
            <Stack spacing={2}>
            <FormLabel htmlFor='email'>Email address</FormLabel>
                <Input 
                placeholder = 'email@example.com' 
                size = 'md' 
                variant = 'filled' 
                width='auto'
                value={email}
                onChange = {(e) => {setEmail(e.target.value)}}
                >
                </Input> 
            
                <FormLabel htmlFor='password'>Password</FormLabel>
                <Input 
                placeholder = 'Password' 
                type = 'password' 
                size = 'md' 
                variant = 'filled' 
                width='auto'
                value = {password}
                onChange = {(e => {setPassword(e.target.value)})}
                >
                </Input> 
            </Stack>
          </FormControl>
        </Center>
      </Container>

      </Box>
    </Center>    

  ); 
}

export default Login; 