import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import LandingScreen from "../screens/LandingScreen";

const Stack = createStackNavigator();

const AppNavigator = () => (
    <NavigationContainer>
        <Stack.Navigator initialRouteName="Landing">
            <Stack.Screen name="Landing" component={LandingScreen} options={{headerShown:false}}/>

        </Stack.Navigator>
    </NavigationContainer>
)

export default AppNavigator;