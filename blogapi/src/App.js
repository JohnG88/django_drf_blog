import React, { useEffect, useState } from 'react';
import './App.css';
import Posts from './components/Posts';
import PostLoading from './components/PostLoaded';
function App() { 
  const PostLoaded = PostLoading(Posts);
	const [appState, setAppState] = useState({loading: false, posts:null})

  useEffect(() => {
	  setAppState({loading: true})
		getApi();
	}, [setAppState])

	const getApi = async () => {
		const response = await fetch('http://127.0.0.1:8000/api/');
		const data = await response.json();
		console.log(data)
		setAppState({loading: false, posts: data})
	}

	return (
    <div className="App">
      <h1>Latest Posts</h1>
			<PostLoaded isLoading={appState.loading} posts={appState.posts}/>
		</div>
  );
}

export default App;
