from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    image_url = "networkhw06/clam.png at main · sungpenny93-creator/networkhw06" 
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>水井村文蛤娃娃 NFT 展示</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; padding: 50px; background-color: #f0f8ff; }}
            .container {{ background-color: white; padding: 30px; border-radius: 15px; box-shadow: 0 0 10px rgba(0,0,0,0.1); display: inline-block; }}
            img {{ max-width: 300px; border-radius: 10px; margin: 20px 0; }}
            h1 {{ color: #0077be; }}
            .code-box {{ text-align: left; background: #333; color: #fff; padding: 10px; border-radius: 5px; margin-top: 20px; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>水井村守護者 (Shuijing Guardian)</h1>
            <p><b>創作理念：</b></p>
            <p>本 NFT 設計概念源自雲林水井村著名的文蛤養殖產業。</p>
            <p>結合區塊鏈技術不可竄改的特性，這隻「科技文蛤」象徵著<br>水井村導入智慧養殖系統，將傳統漁業與未來科技完美結合。</p>
            <p>它不僅是數位藝術品，更是水井村優質水產的數位身分證。</p>
            
            <hr>
            <h3>NFT 預覽圖</h3>
            
            <img src="{image_url}" alt="文蛤 NFT 圖片">
            
            <hr>
            <h3>智能合約 (Smart Contract) 程式碼片段</h3>
            <div class="code-box">
                <pre>
// 這是發行 NFT 的簡易 Solidity 程式碼
pragma solidity ^0.8.0;
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract ShuijingClam is ERC721 {{
    constructor() ERC721("ShuijingClam", "SJC") {{}}
    
    function mintClam(address to, uint256 tokenId) public {{
        _mint(to, tokenId);
    }}
}}
                </pre>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()
