<script setup>
    import { ref, onMounted } from 'vue'
    import { LoaderScript, loadMainScript } from '/src/assets/js/main.js'

    import Navbar from '../components/Navbar.vue'
    import Footer from '../components/Footer.vue'
    import Loader from '../components/Loader.vue'
    import DetailHeader from '../components/DetailHeader.vue'

    import axios from 'axios'

    const textInput = ref('')
    const resItems = ref([])
    const signs = ref([])
    const showSigns = ref([])
    const selectedSigns = ref([])
    const error = ref(false)
    const errorPredict = ref(false)
    const isLogin = ref(true)
    const isFirst = ref(true)

    const textToType = ref("جواب مدل هوشمند:");
    const typedText = ref('');

    const textToTypeSub = ref("متن شما ارسال شده و در حال پیدا کردن مناسب ترین دارو ها برای شما هستم");
    const typedTextSub = ref('');

    const textToTypeSub2 = ref("با توجه به علائم گفته شده دارو های گیاهی:");
    const typedTextSub2 = ref('');

    const textToTypeFoot = ref("برای شما مناسب می باشد امیدوارم جوابم برای شما مفید واقع شود");
    const typedTextFoot = ref('');

    const loadingText = ref(false);

    onMounted(async () => {
        //getIsLogin()
        await loadMainScript()
        await LoaderScript()
    });

    const typeText = () => {
        if (textToType.value.length > 0) {
            typedText.value += textToType.value.charAt(0)
            textToType.value = textToType.value.substring(1)
            setTimeout(typeText, 50)
        }
    }

    const typeTextSub = () => {
        if (textToTypeSub.value.length > 0) {
            typedTextSub.value += textToTypeSub.value.charAt(0)
            textToTypeSub.value = textToTypeSub.value.substring(1)
            setTimeout(typeTextSub, 50)
        }
    }

    const typeTextSub2 = () => {
        if (textToTypeSub2.value.length > 0) {
            typedTextSub2.value += textToTypeSub2.value.charAt(0)
            textToTypeSub2.value = textToTypeSub2.value.substring(1)
            setTimeout(typeTextSub2, 50)
        }
    }

    const typeTextFoot = () => {
        if (textToTypeFoot.value.length > 0) {
            typedTextFoot.value += textToTypeFoot.value.charAt(0)
            textToTypeFoot.value = textToTypeFoot.value.substring(1)
            setTimeout(typeTextFoot, 50)
        }
    }

    const getIsLogin = () => {
        const token = localStorage.getItem('token');
        const user = JSON.parse(localStorage.getItem('user'))
        if (user && token){
            isLogin.value = true
        }
        else{
            isLogin.value = false
        }
    }

    const setToken = () => {
        const token = localStorage.getItem('token');
        if (token) {
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        } else {
            delete axios.defaults.headers.common['Authorization'];
        }
    } 

    const getSignsBaseText = async () => {
        try {
            //setToken()
            typeText()
            typeTextSub()
            console.log({"text": textInput.value})
            const response = await axios.post('http://127.0.0.1:8000/get_signs_by_text', {"text": textInput.value});
            textInput.value = ""
            signs.value = response.data;
            console.log(signs.value)
        } catch (err) {
            console.error('Error medicines fetch:', err)
            errorPredict.value = true
            if(err.response.status == 401){
                error.value = true
            }
        }
        
    }


    const getSignsBaseSigns = async () => {
        try {
            //setToken()
            typeText()
            typeTextSub()
            if (selectedSigns.value.length>0){
                signs.value.push(...selectedSigns.value)
            }
            console.log('signs: ', signs.value)
            const response = await axios.post('http://127.0.0.1:8000/get_signs_by_signs_w2c', 
                                    {"signs": signs.value, "l": 10});
            showSigns.value = response.data;
            console.log('show: ', showSigns.value)
            
        } catch (err) {
            console.error('Error medicines fetch:', err)
            errorPredict.value = true
            if(err.response.status == 401){
                error.value = true
            }
        }
        
    }


    const getMedicineBaseSigns = async () => {
        try {
            //setToken()
            typeText()
            typeTextSub()
            console.log('signs: ', signs.value)
            const response = await axios.post('http://127.0.0.1:8000/get_medicine_by_illnes_w2c', 
                                    {"signs": signs.value, "l": 10});
            resItems.value = response.data;
            console.log('medicines: ', resItems.value)
            
        } catch (err) {
            console.error('Error medicines fetch:', err)
            errorPredict.value = true
            if(err.response.status == 401){
                error.value = true
            }
        }
        
    }


    const predictMedicine = async () => {
        if (textInput.value){
            signs.value = []
            typedText.value = ""
            typedTextSub.value = ""
            typedTextSub2.value = ""
            typedTextFoot.value = ""
            textToType.value = "جواب مدل هوشمند:"
            textToTypeSub.value = "متن شما ارسال شده و در حال پیدا کردن مناسب ترین دارو ها برای شما هستم"
            textToTypeSub2.value = "با توجه به علائم گفته شده شما بیماری زیر را دارید و دارو های گیاهی:"
            textToTypeFoot.value = "برای شما مناسب می باشد امیدوارم جوابم برای شما مفید واقع شود"
            
            if(isFirst.value){
                await getSignsBaseText()
                isFirst.value = false
            }
        }
        
        console.log(selectedSigns.value)
        const noneItemSelected = selectedSigns.value.includes('none')

        if (noneItemSelected){
            await getMedicineBaseSigns()
            typeTextSub2()
            typeTextFoot()
        }
        else{
            loadingText.value = true
            await getSignsBaseSigns()
            loadingText.value = false
        }

        if (signs.value.length>0) {
            errorPredict.value = false
        }
        else{
            errorPredict.value = true
        }
        
    }

    const getHrefTag = (q) => {
        return `/search?q=${q}`
    }

</script>


<template>
        <Navbar></Navbar>

        <DetailHeader img_url="/src/assets/pics/ai-doc.jpg" header_title="بخش هوشمند"></DetailHeader>

        <div v-if="isLogin" class="comment-form-wrap pt-5">
    
            <div class="response mr-5">
                <h3 id="ti-res" class="mb-3 text-success">{{ typedText }}</h3>
                <p id="sub1-res">{{ typedTextSub }}</p>
                <p id="sub2-res">{{ typedTextSub2 }}</p>
                <p class="text-info">{{ resItems.illness }}</p>
                <ul>
                    <li v-for="medicine in resItems.medicines" class="text-success"><router-link :to="getHrefTag(medicine.medicine)">{{ medicine.medicine }}</router-link></li>
                </ul>
                <p id="foot-res">{{ typedTextFoot }}</p>
            </div>
            
            <form @submit.prevent="predictMedicine" class="p-5 bg-light">
                
                <div v-if="isFirst" class="form-group" >
                    <label for="message">لطفا علائم یا بیماری های خود را بنویسید</label>
                    <textarea v-model="textInput" id="message" cols="30" rows="3" class="form-control"></textarea>
                </div>
                <div v-else>
                    <p>از علائم زیر کدام را دارید؟</p>
                    <p v-if="loadingText">لطفا صبر کنید ...</p>
                </div>
                
                <div v-for="item in showSigns" :key="item">
                    <input type="checkbox" v-model="selectedSigns" :value="item" />
                    {{ item }}
                </div>
                <div v-if="showSigns.length">
                    <input type="checkbox" v-model="selectedSigns" value="none" />
                    هیچکدام
                </div>

                <p v-if="errorPredict">متن شما حاوی کلمات مناسب برای تشخیص علائم و بیماری نبود</p>
                <p v-if="error">توکن شما منقضی شده است دوباره <router-link to="/login">وارد</router-link> سایت شوید</p>
                <div class="form-group">
                    <input type="submit" value="ارسال" class="btn py-3 px-4 btn-primary">
                </div>
            </form>
        </div>
        <div v-else>
            <h3 class="mx-5 my-5">برای  استفاده از بخش هوشمند ایتدا باید <router-link to="/login">وارد</router-link> سایت شوید</h3>
        </div>
        

        <Footer></Footer>

        <Loader></Loader>

</template>
  
