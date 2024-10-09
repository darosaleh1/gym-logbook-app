import { View,Text, TextInput, TouchableOpacity } from 'react-native';

const LoginForm = () => (
    <View className="w-full">
      <TextInput
        className="bg-white rounded-lg py-2 px-4 mb-4"
        placeholder="Email"
        placeholderTextColor="#a0aec0"
      />
      <TextInput
        className="bg-white rounded-lg py-2 px-4 mb-4"
        placeholder="Password"
        placeholderTextColor="#a0aec0"
        secureTextEntry
      />
      <TouchableOpacity className="bg-blue-500 rounded-lg py-3">
        <Text className="text-white text-center text-lg font-semibold">
          Login
        </Text>
      </TouchableOpacity>
    </View>
  );

export default LoginForm;