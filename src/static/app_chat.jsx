function subscribe_to_new_answers() {
  var $info = $('#cent-data');
  var centrifuge = new Centrifuge({
    url: $info.data('cent-url'),
    user: $info.data('cent-user').toString(),
    timestamp: $info.data('cent-ts').toString(),
    info: $info.data('cent-info'),
    token: $info.data('cent-token'),
    debug: false,
  });

  var channel = $info.data('cent-channel');
  console.log('subscribe on channel ' + channel);
  centrifuge.subscribe(channel, function(msg) {
    console.log(msg);
    var row_html = '<tr><td>' + msg.data.text + '</td><td>' + msg.data.likes_n + '</td></tr>'
    $('#answers-table tr:last').after(row_html);
  });
  centrifuge.connect();
  return centrifuge;
}

var g_centrifuge = undefined;

$(document).ready(function() {
  g_centrifuge = subscribe_to_new_answers();
});



var config = {
    container: document.getElementsByClassName('b-wall')[0],
};

class Message extends React.Component {
    state = {
        isOpen: false,
    }

    showContent(e) {
        this.setState({isOpen: !this.state.isOpen});
    }

    render () {
        /*let style = {
            border: '4px solid #CCC',
            padding: '1em',
            //background: (this.props.is_published) ? '#FFF' : '#EFEFEF',
        }*/
        return (
            <div>
                <p># {this.props.owner.user.username}</p>
                <p>
                    {this.props.text }
                </p>
            </div>
        )
    }
}

class Chat extends React.Component {
    state = {
        objects: [],
    }

    componentWillMount() {
        this.fetchDataFromServer();
    }

    loadDataFromServer (e) {
        this.fetchDataFromServer();
    }
    fetchDataFromServer() {
        let _this = this;

        fetch('/api/messages/')
            .then(function(response){
                console.log(response);
                response.json().then(function(data){
                    console.log('data', data);
                    _this.setState({objects: data.results || []});
                })
            })
            .catch(function(err){
                console.log('Eror', err);
            })
    }
    render () {
        console.log(this.state);
        return (
            <div>
                {this.state.objects.map((item) => <Message key={item.id} {...item} />)}
            </div>
        )
    }
}

class Root extends React.Component {
    render() {
        let name = (this.props.name) ? this.props.name : 'Dear User';
        return (
            <div>
                <h1>Hello, {name}!</h1>
                <Chat />
            </div>
        )
    }
}

ReactDOM.render(<Root />, config.container
    //<h1>ggg</h1>,
    //document.getElementsByClassName('b-wall')[0]
);
