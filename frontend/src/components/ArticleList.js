import React from 'react';
import { useCookies } from 'react-cookie';
import APIService from '../APIService';


function ArticleList(props) {

    const [token] = useCookies(['mytoken'])

    const editBtn = (article) => {
        props.editBtn(article)
    }

    const deleteBtn = (article) => {
        APIService.DeleteArticle(article.id, token['mytoken'])
        .then(() => props.deleteBtn(article))
        .catch(error => console.log(error))
    }

    return (
        <div>

            {props.articles && props.articles.map(article => {
                return (
                    <div key = {article.id}>
                        <h2>{article.title}</h2>
                        <p>{article.description}</p>
                        
                        <div className="row">
                            <div className="col-md-2">
                                <button className="btn btn-primary" onClick = {() => editBtn(article)}>Update</button>
                            </div>

                            <div className="col">
                                <button className="btn btn-danger" onClick ={() => deleteBtn(article)}>Delete</button>
                            </div>

                        </div>

                        <hr className="hrclass"/>
                    </div>
                )
            })}
            
        </div>
    )
}

export default ArticleList
