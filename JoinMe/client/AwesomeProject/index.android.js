/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 */
'use strict';

var React = require('react-native');
var SearchPage = require('./SearchPage');

var {
  AppRegistry,
  StyleSheet,
  Text,
  View,
} = React;

class PropertyFinderApp extends React.Component {
  render() {
    return (
	<React.Text style={styles.text}>
		Hello World (Again)
		</React.Text>
	);
  }
}
var AwesomeProject = React.createClass({
  render: function() {
    return (
	<React.Navigator 
		initialRoute={{name: 'My First Scene', index: 0}} 
		renderScene={(route, navigator) => 
			<SearchPage 
			name={route.name} 
			onForward={() => { var nextIndex = route.index + 1; navigator.push({ name: 'Scene ' + nextIndex, index: nextIndex, }); }} 
			onBack={() => { if (route.index > 0) { navigator.pop(); } }} /> } 
		/>
    );
  }
});

var styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
});

AppRegistry.registerComponent('AwesomeProject', () => AwesomeProject);
