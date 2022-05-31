import { promises } from 'fs'
import path from 'path';
import express from 'express'
import cors from 'cors'


const __dirname = path.resolve();


var caminhoArq = __dirname+'\\PangyaTxt\\PangyaValues.txt'
 
async function  addNumInput(caminhoArq)
{
  
   return await promises.readFile(caminhoArq,'utf-8')
}

const app = express()
app.use(cors())
const port = 3000
 
 app.get('/', async (req, res) => {
   var listaResultado = await addNumInput(caminhoArq)
   listaResultado = listaResultado.split('\r\n').filter((linha)=>
   {
      if(linha == '')
      {
         return false
      }
      else{
         return true
      }
   })
   res.send(listaResultado)
 })
 app.listen(port, () => {
  
 })