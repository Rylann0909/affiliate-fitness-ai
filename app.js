// app.js - loads products.json and displays them in a simple scrolling feed

async function loadProducts() {
  try {
    const resp = await fetch('site/products.json?_=' + Date.now());
    const data = await resp.json();
    return data.products || [];
  } catch (e) {
    console.error('Could not load products.json', e);
    return [];
  }
}

function buildCard(p) {
  const card = document.createElement('article');
  card.className = 'card';
  const preview = document.createElement('div');
  preview.className = 'preview';
  if (p.video) {
    const vid = document.createElement('video');
    vid.src = p.video.replace('../','');
    vid.controls = true;
    vid.loop = false;
    preview.appendChild(vid);
  } else if (p.image) {
    const img = document.createElement('img');
    img.src = p.image.replace('../','');
    preview.appendChild(img);
  }
  const info = document.createElement('div');
  info.className = 'info';
  const h = document.createElement('h2');
  h.textContent = p.title;
  const desc = document.createElement('p');
  desc.textContent = p.description;
  const btn = document.createElement('a');
  btn.className = 'buy-btn';
  btn.textContent = 'Buy Now';
  btn.href = p.affiliate_url;
  btn.target = '_blank';
  btn.rel = 'noopener noreferrer nofollow';
  const small = document.createElement('div');
  small.className = 'small';
  small.textContent = `Price: $${p.price} • Source: ${p.affiliate_source}`;
  info.appendChild(h);
  info.appendChild(desc);
  info.appendChild(btn);
  info.appendChild(small);
  card.appendChild(preview);
  card.appendChild(info);
  return card;
}

async function init() {
  const products = await loadProducts();
  const container = document.getElementById('carousel');
  if (!products || products.length === 0) {
    container.innerHTML = '<p style="opacity:.8">No products yet — run the generator.</p>';
    return;
  }
  products.forEach(p => {
    container.appendChild(buildCard(p));
  });
}

document.addEventListener('DOMContentLoaded', init);
