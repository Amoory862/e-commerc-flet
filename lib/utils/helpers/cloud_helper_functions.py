import firebase_admin
from firebase_admin import credentials, storage
from typing import Optional, List, Union

# Initialize Firebase Admin SDK
cred = credentials.Certificate('path/to/your/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'your-project-id.appspot.com'
})

class TCloudHelperFunctions:
    @staticmethod
    def check_single_record_state(snapshot: Optional[Union[dict, None]]) -> str:
        """Check the state of a single database record."""
        if snapshot is None:
            return 'No Data Found!'
        elif isinstance(snapshot, Exception):
            return 'Something went wrong.'
        return ''

    @staticmethod
    def check_multi_record_state(
        snapshot: Optional[List[dict]], 
        loader: Optional[str] = None, 
        error: Optional[str] = None, 
        nothing_found: Optional[str] = None
    ) -> str:
        """Check the state of multiple (list) database records."""
        if snapshot is None:
            if loader:
                return loader
            return 'Loading...'
        elif not snapshot:
            if nothing_found:
                return nothing_found
            return 'No Data Found!'
        elif isinstance(snapshot, Exception):
            if error:
                return error
            return 'Something went wrong.'
        return ''

    @staticmethod
    async def get_url_from_file_path_and_name(path: str) -> str:
        """Retrieve the download URL from a file path and name."""
        try:
            if not path:
                return ''
            bucket = storage.bucket()
            blob = bucket.blob(path)
            return blob.public_url
        except Exception as e:
            raise Exception(str(e)) from e

    @staticmethod
    async def get_url_from_uri(uri: str) -> str:
        """Retrieve the download URL from a given storage URI."""
        try:
            if not uri:
                return ''
            bucket = storage.bucket()
            blob = bucket.blob(uri.split('/')[-1])
            return blob.public_url
        except Exception as e:
            raise Exception(str(e)) from e
