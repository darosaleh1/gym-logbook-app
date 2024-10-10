import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, Alert } from 'react-native';
import * as UserService from "../services/user.js"

const SignupScreen = ({navigation}) => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleSignup = async () => {
    try {
      const response = await UserService.signup(username,email,password,confirmPassword);
      console.log(response.data)
      navigation.navigate('Login')
    } catch (error) {
      Alert.alert('Error', error.response?.data?.message || 'Signup failed');
    }
  };

  return (
    <View className="flex-1 bg-blue-950 justify-center items-center p-6">
      <View className="w-full">
        <TextInput
          className="bg-white rounded-lg py-2 px-4 mb-4"
          placeholder="Username"
          placeholderTextColor="#a0aec0"
          value={username}
          onChangeText={setUsername}
        />
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
        <TextInput
          className="bg-white rounded-lg py-2 px-4 mb-4"
          placeholder="Confirm Password"
          placeholderTextColor="#a0aec0"
          value={confirmPassword}
          onChangeText={setConfirmPassword}
          secureTextEntry
        />
        <TouchableOpacity className="bg-green-500 rounded-lg py-3" onPress={handleSignup}>
          <Text className="text-white text-center text-lg font-semibold">
            Signup
          </Text>
        </TouchableOpacity>
        <TouchableOpacity onPress={()=> navigation.navigate('Login')}>

        <Text className="text-white text-center mt-4 underline">
            Already have an account? Login
        </Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

export default SignupScreen;