<template>
    <div class="form" v-if="!this.statusSendData">
        <div class="form-label">Заполните заявку на регистрацию</div>

        <div>
            <select v-model="this.sex" class="form-select">
                <option disabled value="" selected="selected">Выберите пол</option>
                <option value="мужской">мужской</option>
                <option value="женский">женский</option>
            </select>
        </div>

        <div>
            <input v-model="this.age"  class="form-input" placeholder="Возраст" type="number">
        </div>

        <div>
            <select v-model="this.status" class="form-select">
                <option disabled value="" selected="selected">Выберите статус</option>
                <option value="учащийся в школе">учащийся в школе</option>
                <option value="студент">студент</option>
                <option value="гражданин ищущий работу">гражданин ищущий работу</option>
            </select>
        </div>

        <button @click="this.sendData()" v-if="this.sex != '' && this.age != '' && this.status != ''" class="send-data">
            Отправить заявку
        </button>
    </div>

    <!-- что видит пользователь после отправик заявки -->
    <div class="thanks"  v-if="this.statusSendData">
        <h2 class="thanks-label">Спасибо, что отправили заявку!</h2>
    </div>

</template>

<script>
import axiox from 'axios';

export default{
    data(){
        return {
            town : this.$route.params.town,
            czn : this.$route.params.czn,
            sex: "",
            age: "",
            status: "",
            statusSendData: false
        }
    },

    methods: {
        sendData(){
            axiox.post("https://sobesedka.site/api/v1/send_person_data",{
              "sex": this.sex,
              "age":  this.age,
              "status": this.status,
              "town": this.town,
              "czn": this.czn
            })
            this.statusSendData = true
        }
    }

}
</script>

<style>
.form{
    text-align: center;
    margin-top: 20px;
}

.thanks{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 200px;
    text-align: center;
}

.thanks-label{
    color: var(--main-dark-blue-color)
}

.form-input{
    min-width: 295px;
    min-height: 45px;
    border: 3px solid var(--main-dark-blue-color);
    margin-top: 10px;
    border-radius: 10px;
    text-align: center;
}

.form-input::placeholder{
    text-align: center;
}

.form-select{
    min-width: 300px;
    min-height: 50px;
    border: 3px solid var(--main-dark-blue-color);
    margin-top: 10px;
    border-radius: 10px;
    text-align: center;
}

.send-data{
    min-width: 300px;
    min-height: 50px;  
    border: 3px solid var(--main-dark-blue-color);
    border-radius: 10px;
    color: white;
    background-color: var(--main-dark-blue-color);
    font-weight: bold;
    margin-top: 10px;
}
</style>