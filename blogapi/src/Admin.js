import React, { useEffect, useState } from 'react';
import './App.css';
import Posts from './components/admin/Posts';
import PostLoading from './components/posts/PostLoaded';
import axiosInstance from './axios';

function Admin() {
	const PostLoaded = PostLoading(Posts);
	const [appState, setAppState] = useState({loading: true, posts: null,});

	useEffect(() => {
    axiosInstance.get().then((res) => {
			const allPosts = res.data;
			setAppState({loading: false, posts: allPosts});
			console.log(res.data);
		});
	}, [setAppState]);
	
	return (
		<div className="App">
      <h1>Latest Posts</h1>
			<PostLoaded isLoading={appState.loading} posts={appState.posts}/> 
		</div>
	);
}

export default Admin;
