import React from 'react';
//This a wrapper for Posts
function PostLoading(Component) {
	return function PostLoadingComponent({isLoading, ...props}) {
    if (!isLoading) return <Component {...props} />
			return (
				<p style={{ fontSize: '25px' }}>
          We are waiting for the data to load! ...
				</p>
			);
	};
}

export default PostLoading;
