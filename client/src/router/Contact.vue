<script setup>
    import { ref, onMounted } from 'vue'
    import { LoaderScript, loadMainScript } from '/src/assets/js/main.js'

    import Navbar from '../components/Navbar.vue'
    import Slider from '../components/Slider.vue'
    import Tozihat from '../components/Tozihat.vue'
    import CategoryCard from '../components/CategoryCard.vue'
    import Footer from '../components/Footer.vue'
    import Banner from '../components/Banner.vue'
    import Loader from '../components/Loader.vue'
    import Nazarsanji from '../components/Nazarsanji.vue'

    onMounted( async () => {
        await loadMainScript()
        await LoaderScript()
        console.log("loaded")
    });

</script>


<template>
        <Navbar></Navbar>

        <div class="hero-wrap hero-bread" style="background-image: url('/src/assets/pics/bg_1.jpg');">
      <div class="container">
        <div class="row no-gutters slider-text align-items-center justify-content-center">
          <div class="col-md-9 ftco-animate text-center">
          	<p class="breadcrumbs"><span class="mr-2"><a href="index.html">خانه</a></span> </p>
            <h1 class="mb-0 bread">ارتباط با ما</h1>
          </div>
        </div>
      </div>
    </div>

    <section class="ftco-section contact-section bg-light">
      <div class="container">
      	<div class="row d-flex mb-5 contact-info">
          <div class="w-100"></div>
          <div class="col-md-3 d-flex">
          	<div class="info bg-white p-4">
	            <p><span>آدرس:</span> ایران - تهران - بلوار جمهوری</p>
	          </div>
          </div>
          <div class="col-md-3 d-flex">
          	<div class="info bg-white p-4">
	            <p><span>تلفن:</span> <a href="tel://1234567920">02112345678</a></p>
	          </div>
          </div>
          <div class="col-md-3 d-flex">
          	<div class="info bg-white p-4">
	            <p><span>ایمیل:</span> <a href="mailto:info@yoursite.com">email@website.com</a></p>
	          </div>
          </div>
          <div class="col-md-3 d-flex">
          	<div class="info bg-white p-4">
	            <p><span>وب سایت</span> <a href="#">webrubik.com</a></p>
	          </div>
          </div>
        </div>
        <div class="row block-9">
          <div class="col-md-6 order-md-last d-flex">
            <form action="#" class="bg-white p-5 contact-form">
              <div class="form-group">
                <input type="text" class="form-control" placeholder="نام">
              </div>
              <div class="form-group">
                <input type="text" class="form-control" placeholder="ایمیل">
              </div>
              <div class="form-group">
                <input type="text" class="form-control" placeholder="موضوع">
              </div>
              <div class="form-group">
                <textarea name="" id="" cols="30" rows="7" class="form-control" placeholder="پیام"></textarea>
              </div>
              <div class="form-group">
                <input type="submit" value="ارسال پیام" class="btn btn-primary py-3 px-5">
              </div>
            </form>
          
          </div>

          <div class="col-md-6 d-flex">
          	<div id="map" class="bg-white"></div>
          </div>
        </div>
      </div>
    </section>

        <Footer></Footer>

        <Loader></Loader>

</template>
  
