<template>
    <v-container
        fluid
    >
        <v-layout>
            <v-flex v-if="loading">
                <carregando
                    :text="'Carregando dados da edição'"
                />
            </v-flex>
            <v-flex
                v-else
                xs10
                offset-xs1
            >
                <v-form
                    v-model="valid"
                >
                    <v-card
                        class="pl-3"
                    >
                        <v-card-title>
                            <div class="headline">
                                Edição de área
                            </div>
                        </v-card-title>
                        <v-text-field
                            v-model="dadosArea.nome"
                            label="Nome"
                            @change="atualizarCampo('nome', $event)"
                        />
                        <v-select
                            v-model="dadosArea.localidade"
                            :items="getAreaMetadata.localidade"
                            item-text="descricao"
                            item-value="valor"
                            label="Localidade"
                            @change="atualizarCampo('localidade', $event)"
                        />
                        <v-text-field
                            v-model="dadosArea.dimensao"
                            label="Dimensão"
                            @change="atualizarCampo('dimensao', $event)"
                        />
                        <v-text-field
                            v-model="dadosArea.largura"
                            label="Largura"
                            @change="atualizarCampo('largura', $event)"
                        />
                        <v-text-field
                            v-model="dadosArea.comprimento"
                            label="comprimento"
                            @change="atualizarCampo('comprimento', $event)"
                        />
                    </v-card>
                    <v-card
                        class="pa-3"
                    >
                        <v-select
                            v-model="dadosArea.solo_predominante"
                            :items="getAreaMetadata.solo"
                            item-text="descricao"
                            item-value="valor"
                            label="Solo predominante"
                            @change="atualizarCampo('Solo predominante', $event)"
                        />
                        <v-select
                            v-model="dadosArea.declividade_predominante"
                            :items="getAreaMetadata.declividade"
                            item-text="descricao"
                            item-value="valor"
                            label="Declividade predominante"
                            @change="atualizarCampo('declividade_predominante', $event)"
                        />
                        <v-select
                            v-model="dadosArea.microclima"
                            :items="getAreaMetadata.microclimas"
                            item-text="descricao"
                            item-value="valor"
                            label="Microclima"
                            @change="atualizarCampo('microclima', $event)"
                        />
                    </v-card>
                    <v-btn
                        color="info"
                        @click="salvar()"
                    >
                        <v-icon
                            class="pr-3"
                        >save</v-icon>
                        salvar
                    </v-btn>
                    <v-btn
                        color="error"
                        @click="voltar()"
                    >
                        <v-icon
                            class="pr-3"
                        >cancel</v-icon>
                        cancelar
                    </v-btn>
                </v-form>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import _ from 'lodash';
import Carregando from '@/components/CarregandoVuetify';
import Tools from '@/mixins/tools';
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'EditarArea',
    components: {
        Carregando,
    },
    mixins: [
        Tools,
    ],
    data() {
        return {
            valid: true,
            dadosEditados: {
                id: '',
                nome: '',
                dimensao: '',
                largura: '',
                comprimento: '',
                solo_predominante: '',
                declividade_predominante: '',
                localidade: '',
                microclima: '',
            },
            loaded: {
                dados: false,
                metadados: false,
            },
            loading: true,
        };
    },
    computed: {
        ...mapGetters({
            dadosArea: 'area/area',
            getAreaMetadata: 'area/getAreaMetadata',
        }),
        id() {
            return this.$route.params.id;
        },
    },
    watch: {
        dadosArea() {
            if (this.dadosArea.id !== 'undefined') {
                this.loaded.dados = true;
                this.inicializarDadosArea();
            }
        },
        getAreaMetadata() {
            if (this.getAreaMetadata.id !== 'undefined') {
                this.loaded.metadados = true;
            }
        },
        loaded: {
            handler(value) {
                const fullyLoaded = _.keys(value).every(i => value[i]);
                if (fullyLoaded) {
                    this.loading = false;
                }
            },
            deep: true,
        },
    },
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscarArea(this.$route.params.id);
            this.buscarAreaMetadata();
        }
    },
    methods: {
        ...mapActions({
            buscarArea: 'area/buscarArea',
            buscarAreaMetadata: 'area/buscarAreaMetadata',
            updateArea: 'area/updateArea',
        }),
        inicializarDadosArea() {
            this.dadosEditados = {
                id: this.dadosArea.id,
                nome: this.dadosArea.nome,
                dimensao: this.dadosArea.dimensao,
                largura: this.dadosArea.largura,
                comprimento: this.dadosArea.comprimento,
                solo_predominante: this.dadosArea.solo_predominante,
                declividade_predominante: this.dadosArea.declividade_predominante,
                localidade: this.dadosArea.localidade,
                microclima: this.dadosArea.microclima,
            };
        },
        atualizarCampo(key, value) {
            if (Object.keys(this.dadosEditados).includes(key)) {
                this.dadosEditados[key] = value;
            }
        },
        salvar() {
            this.updateArea(this.dadosEditados);
        },
    },
};
</script>
