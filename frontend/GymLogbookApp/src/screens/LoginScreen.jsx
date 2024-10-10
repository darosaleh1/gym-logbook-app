import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, Alert } from 'react-native';
import * as UserService from "../services/user.js"
 
const LoginScreen = ({navigation}) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      const response = await UserService.login(email,password);
      console.log(response.data)
      navigation.navigate('Home')



      // Handle successful login (e.g., store token, navigate to main screen)
    } catch (error) {
      Alert.alert('Error', error.response?.data?.message || 'Login failed');
    }
  };

  return (
    <View className="flex-1 bg-blue-950 justify-center items-center p-6">
      <View className="w-full">
        <TextInput
          className="bg-white rounded-lg py-2 px-4 mb-4"
          placeholder="Email"
          placeholderTextColor="#a0aec0"
          value={email}
          onChangeText={setEmail}
          keyboardType="email-address"
          autoCapitalize="none"
        />
        <TextInput
          className="bg-white rounded-lg py-2 px-4 mb-4"
          placeholder="Password"
          placeholderTextColor="#a0aec0"
          value={password}
          onChangeText={setPassword}
          secureTextEntry
        />
        <TouchableOpacity className="bg-blue-500 rounded-lg py-3" onPress={handleLogin}>
          <Text className="text-white text-center text-lg font-semibold">
            Login
          </Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={()=> navigation.navigate('Signup')}>

        <Text className="text-white text-center mt-4 underline">
            Need to make an account? Signup
        </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default LoginScreen;