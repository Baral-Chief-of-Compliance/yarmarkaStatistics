<template>
    <div class="form">
        <div class="form-label">Заполните заявку на регистрацию</div>

        <div>
            <select class="form-select">
                <option disabled value="" selected="selected">Выберите пол</option>
                <option value="мужской">мужской</option>
                <option value="женский">женский</option>
            </select>
        </div>

        <div>
            <input class="form-input" placeholder="Возраст" type="number">
        </div>

        <div>
            <select class="form-select">
                <option disabled value="" selected="selected">Выберите статус</option>
                <option value="учащийся в школе">учащийся в школе</option>
                <option value="студент">студент</option>
                <option value="гражданин ищущий работу">гражданин ищущий работу</option>
            </select>
        </div>
        <button>
            sds
        </button>

    </div>

</template>

<style>
.form{
    text-align: center;
    margin-top: 20px;

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
</style>