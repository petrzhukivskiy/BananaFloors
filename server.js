import express from 'express';
import OpenAI from 'openai';
import fs from 'node:fs';

const app = express();
app.set('trust proxy', 1);
app.use(express.json({ limit: '8kb' }));
const knowledge = JSON.parse(fs.readFileSync(new URL('./site-knowledge.json', import.meta.url), 'utf8'));
const client = process.env.OPENAI_API_KEY ? new OpenAI({ apiKey: process.env.OPENAI_API_KEY }) : null;
const model = process.env.OPENAI_MODEL || 'gpt-5.5';
const buckets = new Map();
function allowed(ip){
  const now=Date.now(), windowMs=15*60*1000, max=30;
  const b=buckets.get(ip)||{start:now,count:0};
  if(now-b.start>windowMs){b.start=now;b.count=0;}
  b.count++; buckets.set(ip,b); return b.count<=max;
}
app.get('/api/health',(req,res)=>res.json({ok:true,ai:Boolean(client)}));
app.post('/api/ask', async (req,res)=>{
  if(!allowed(req.ip)) return res.status(429).json({error:'Too many requests. Please try again later.'});
  const message=String(req.body?.message||'').trim().slice(0,500);
  if(!message) return res.status(400).json({error:'Question required.'});
  if(!client) return res.status(503).json({error:'AI is not configured on this server.'});
  try{
    const response=await client.responses.create({
      model,
      instructions:`You are Ask Banana, the concise flooring assistant for Banana Floors in the Portland metro. Use ONLY the supplied business knowledge for company-specific facts, pricing, specs, service area and process. Do not invent reviews, guarantees, licenses, warranties, exact product availability, exact installation prices or project conditions. Material ranges are planning estimates only. When a question requires a project-specific installation price, explain what affects it and invite the user to request an estimate or call/text 503-421-1730. Keep answers friendly, practical, usually under 120 words. Business knowledge:\n${JSON.stringify(knowledge)}`,
      input: message
    });
    res.json({answer:response.output_text});
  }catch(err){
    console.error(err?._request_id||'', err?.message||err);
    res.status(500).json({error:'Assistant unavailable. Please try again.'});
  }
});
const port=Number(process.env.PORT||3001);
app.listen(port,'127.0.0.1',()=>console.log(`Banana AI listening on 127.0.0.1:${port}`));
