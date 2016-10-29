var config = {
    container: document.getElementsByClassName('b-wall')[0],
};

class Post extends React.Component {
    state = {
        isOpen: false,
    }

    showContent(e) {
        this.setState({isOpen: !this.state.isOpen});
    }

    render () {
        let style = {
            border: '4px solid #CCC',
            padding: '1em',
            //background: (this.props.is_published) ? '#FFF' : '#EFEFEF',
        }
        return (
                <p style={style} className="class_post" 
                    onClick={this.showContent.bind(this)}>
                    {(this.state.isOpen) ? this.props.text : this.props.text.slice(0, 50)}
                    <a href={`/posts/${this.props.id}`}>See full</a>
                </p>
        )
    }
}

class PostList extends React.Component {
    state = {
        objects: [],
        text: '',
    }

    componentWillMount() {
        this.fetchDataFromServer();
    }

    onSearch(content) {
        this.setState({text: content});
        this.fetchDataFromServer();
    }

    loadDataFromServer (e) {
        this.fetchDataFromServer();
    }
    fetchDataFromServer() {
        let _this = this;

        fetch('/api/posts/?text=' + this.state.text || '')
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
                <PostSearch 
                    onButtonClick={this.loadDataFromServer.bind(this)}
                    onSearch={this.onSearch.bind(this)}/>
                {this.state.objects.map((item) => <Post key={item.id} {...item} />)} 
            </div>
        )
    }
}

class PostSearch extends React.Component {
    state = {
        content: '',
    }

    onChangeContent (e) {
        console.log(e, this);
        this.setState({content: e.target.value});
        this.props.onSearch(e.target.value);
    }

    render() {
        return (
            <div>
                <label htmlFor="id_search">Search string</label>&nbsp;
                <input
                    onChange={this.onChangeContent.bind(this)}
                    id="id_search"
                    type="text"
                    size="30"
                    value={this.state.content}
                    placeholder="search for" />
                <button onClick={this.props.onButtonClick.bind(this)}>Go</button>
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
                <PostList />
            </div>
        )
    }
}

ReactDOM.render(<Root />, config.container
    //<h1>ggg</h1>,
    //document.getElementsByClassName('b-wall')[0]
);
