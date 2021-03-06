/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 */
'use strict';

var React = require('react-native'); 
var {
  StyleSheet,
  Text,
  TextInput,
  View,
  TouchableHighlight,
  ActivityIndicatorIOS,
  Image,
  Component
} = React;

class SearchPage extends Component {
	
	constructor(props) {
    super(props);
    this.state = {
      searchString: 'london',
      isLoading: false,
      message: ''
    };
  }
	onLocationPressed() {
	  navigator.geolocation.getCurrentPosition(
		location => {
		  var search = location.coords.latitude + ',' + location.coords.longitude;
		  this.setState({ searchString: search });
		},
		error => {
		  this.setState({
			message: 'There was a problem with obtaining your location: ' + error
		  });
		});
	}
	onSearchTextChanged(event) {
    this.setState({ searchString: event.nativeEvent.text });
	}
  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.description}>
          Search for houses to buy!
        </Text>
        <Text style={styles.description}>
          Search by place-name, postcode or search near your location.
        </Text>
		<View style={styles.flowRight}>
		  <TextInput
            style={styles.searchInput}
            placeholder='Search via name or postcode'
            value={this.state.searchString}
            onChange={this.onSearchTextChanged.bind(this)}/>
		  <TouchableHighlight style={styles.button}
			  underlayColor='#99d9f4'>
			<Text style={styles.buttonText}>Go</Text>
		  </TouchableHighlight>
		</View>
		<TouchableHighlight style={styles.button}
		onPress={this.onLocationPressed.bind(this)}
			underlayColor='#99d9f4'>
		  <Text style={styles.buttonText}>Location</Text>
		</TouchableHighlight>
		<Text style={styles.description}>{this.state.message}</Text>
      </View> 
    );
  }
}

var styles = StyleSheet.create({
  description: {
    marginBottom: 20,
    fontSize: 18,
    textAlign: 'center',
    color: '#656565'
  },
  container: {
    padding: 30,
    marginTop: 65,
    alignItems: 'center'
  },
	flowRight: {
	  flexDirection: 'row',
	  alignItems: 'center',
	  alignSelf: 'stretch'
	},
	buttonText: {
	  fontSize: 18,
	  color: 'white',
	  alignSelf: 'center'
	},
	button: {
	  height: 36,
	  flex: 1,
	  flexDirection: 'row',
	  backgroundColor: '#48BBEC',
	  borderColor: '#48BBEC',
	  borderWidth: 1,
	  borderRadius: 8,
	  marginBottom: 10,
	  alignSelf: 'stretch',
	  justifyContent: 'center'
	},
	searchInput: {
	  height: 36,
	  padding: 4,
	  marginRight: 5,
	  flex: 4,
	  fontSize: 18,
	  borderWidth: 1,
	  borderColor: '#48BBEC',
	  borderRadius: 8,
	  color: '#48BBEC'
	}
});

module.exports = SearchPage;